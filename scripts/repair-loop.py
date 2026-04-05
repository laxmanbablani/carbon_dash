import subprocess
import os
import sys
import time
import re
import json

def run_command(command, shell=True):
    print(f"Running: {command}")
    try:
        result = subprocess.run(command, shell=shell, capture_output=True, text=True, timeout=30)
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired as e:
        return -1, e.stdout if e.stdout else "", e.stderr if e.stderr else "Timeout"
    except Exception as e:
        return -1, "", str(e)

def get_missing_component(stderr):
    # AttributeError: module 'carbon_dash' has no attribute 'AISkeleton'
    match = re.search(r"AttributeError: module 'carbon_dash' has no attribute '(\w+)'", stderr)
    if match:
        return match.group(1)
    return None

def get_invalid_prop(stderr):
    # TypeError: Button() got an unexpected keyword argument 'href'
    match = re.search(r"TypeError: (\w+)\(\) got an unexpected keyword argument '(\w+)'", stderr)
    if match:
        return match.group(1), match.group(2)
    return None

def update_config(missing_comp=None, invalid_prop=None):
    config_path = 'scripts/config.json'
    with open(config_path, 'r') as f:
        config = json.load(f)

    changed = False
    if missing_comp:
        # Check if it's already there, maybe it needs an export fix
        if missing_comp not in config:
            print(f"Adding missing component to config: {missing_comp}")
            # We don't know the exact props yet, but generate.js can try to extract them if we add it to config
            # Actually, generate.js currently iterates over @carbon/react exports
            # If it's missing from carbon_dash, it might be because it's not in config OR not exported from @carbon/react
            # If the user wants full coverage, we might need to force it in config
            config[missing_comp] = {
                "injectProps": ["id", "className", "style", "children"]
            }
            changed = True
    
    if invalid_prop:
        comp_name, prop_name = invalid_prop
        print(f"Handling invalid prop '{prop_name}' for '{comp_name}'")
        # For now, if a prop is invalid in Python, we might want to skip it in generate-docs.js
        # But here we are fixing the library. If it's a valid Carbon prop but missing in Dash,
        # it means propTypes extraction failed or it's a special prop.
        # We can try to add it to skip list in generate-docs.js if it's truly invalid.
    
    if changed:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
    return changed

def main():
    max_iterations = 10
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        print(f"\n--- Iteration {iteration} ---")
        
        # 1. Regenerate components
        print("Regenerating components...")
        rc, out, err = run_command("node scripts/generate.js")
        if rc != 0:
            print(f"Generation failed:\n{err}")
            # If generation fails, we might have a JS error to fix
            break
            
        # 2. Build
        print("Building...")
        rc, out, err = run_command("npm run build")
        if rc != 0:
            print(f"Build failed:\n{err}")
            # Check for JS syntax errors in generated files
            break
            
        # 3. Generate gallery
        print("Generating gallery...")
        rc, out, err = run_command("node scripts/generate-docs.js")
        if rc != 0:
            print(f"Gallery generation failed:\n{err}")
            break
            
        # 4. Try to run gallery and catch first error
        print("Testing gallery...")
        # We use a small script to just import and initialize the stories_dict to catch errors
        test_script = """
import sys
import os
sys.path.append(os.getcwd())
try:
    import docs.gallery
    print("SUCCESS")
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)
"""
        with open("_test_gallery.py", "w") as f:
            f.write(test_script)
            
        rc, out, err = run_command("python3 _test_gallery.py")
        
        if "SUCCESS" in out:
            print("Gallery is stable!")
            break
        else:
            print("Gallery failed. Parsing error...")
            missing_comp = get_missing_component(err)
            invalid_prop = get_invalid_prop(err)
            
            if missing_comp:
                print(f"Found missing component: {missing_comp}")
                update_config(missing_comp=missing_comp)
            elif invalid_prop:
                comp, prop = invalid_prop
                print(f"Found invalid prop: {comp}.{prop}")
                # For invalid props in the gallery, we might need to update generate-docs.js 
                # to skip them if they aren't in the component's API
                # Or fix the component if it SHOULD have it.
                # Since the gallery is auto-generated from stories, it might be using props 
                # that our wrapper doesn't support yet.
                
                # Let's try a simple fix: add the prop to generate-docs.js skip list if it keeps failing
                # For now, let's just log it.
                break 
            else:
                print(f"Unknown error:\n{err}")
                break

    if os.path.exists("_test_gallery.py"):
        os.remove("_test_gallery.py")

if __name__ == "__main__":
    main()
