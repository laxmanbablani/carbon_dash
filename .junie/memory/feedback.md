[2026-04-05 12:34] - Updated by Junie
{
    "TYPE": "positive",
    "CATEGORY": "Scope and coverage",
    "EXPECTATION": "Extend automation beyond a single component and aim for full coverage of @carbon/react components.",
    "NEW INSTRUCTION": "WHEN running generation pipeline THEN process all @carbon/react components for wrappers and tests"
}

[2026-04-05 12:35] - Updated by Junie
{
    "TYPE": "positive",
    "CATEGORY": "Scope and coverage",
    "EXPECTATION": "Expand automation beyond a single component and achieve full coverage of @carbon/react.",
    "NEW INSTRUCTION": "WHEN running generation pipeline THEN process all @carbon/react components for wrappers and tests"
}

[2026-04-05 12:37] - Updated by Junie
{
    "TYPE": "positive",
    "CATEGORY": "Scope and coverage",
    "EXPECTATION": "Expand automation beyond a single component and aim for full coverage of @carbon/react.",
    "NEW INSTRUCTION": "WHEN running generation pipeline THEN process all @carbon/react components for wrappers and tests"
}

[2026-04-05 12:37] - Updated by Junie
{
    "TYPE": "positive",
    "CATEGORY": "Scope and coverage",
    "EXPECTATION": "Automate beyond a single component and target full coverage of @carbon/react.",
    "NEW INSTRUCTION": "WHEN running generation pipeline THEN process all @carbon/react components for wrappers and tests"
}

[2026-04-05 12:38] - Updated by Junie
{
    "TYPE": "positive",
    "CATEGORY": "Scope and coverage",
    "EXPECTATION": "Expand automation beyond a single component and achieve full coverage of @carbon/react.",
    "NEW INSTRUCTION": "WHEN running generation pipeline THEN process all @carbon/react components for wrappers and tests"
}

[2026-04-05 12:40] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Documentation cleanup",
    "EXPECTATION": "AGENTS.md should be the single, conflict-free source of truth and be updated with noteworthy findings before continuing work.",
    "NEW INSTRUCTION": "WHEN starting new implementation work THEN reconcile and remove conflicts in AGENTS.md first"
}

[2026-04-05 12:48] - Updated by Junie
{
    "TYPE": "preference",
    "CATEGORY": "Iterative automation",
    "EXPECTATION": "Continuously run the harness across all components, investigate issues, evolve the harness, and record noteworthy findings in AGENTS.md each pass for 20–30 iterations.",
    "NEW INSTRUCTION": "WHEN a generation pass finishes THEN update AGENTS.md findings and start next pass"
}

[2026-04-05 13:15] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Undefined components handling",
    "EXPECTATION": "Ensure the generation/build pipeline prevents or handles undefined Carbon components to avoid the 'Element type is invalid' runtime error.",
    "NEW INSTRUCTION": "WHEN generating wrappers THEN verify Carbon import exists and fail build if undefined"
}

[2026-04-05 13:15] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Undefined elements prevention",
    "EXPECTATION": "The automated build must detect undefined Carbon components and prevent the runtime 'Element type is invalid' error.",
    "NEW INSTRUCTION": "WHEN running generation pipeline THEN validate @carbon/react exports and abort on missing"
}

[2026-04-05 13:16] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Undefined elements prevention",
    "EXPECTATION": "The generation/build process must detect undefined Carbon components and stop before runtime errors occur.",
    "NEW INSTRUCTION": "WHEN generating fragments THEN assert imported Carbon component is defined and exit on failure"
}

[2026-04-05 13:19] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery examples completeness",
    "EXPECTATION": "The gallery should show realistic examples: labeled buttons, disabled states, range slider, and all four DataTable variants, ideally mirroring Carbon stories.",
    "NEW INSTRUCTION": "WHEN updating gallery.py THEN include labels, disabled props, range slider, and DataTable variants"
}

[2026-04-05 13:19] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery completeness",
    "EXPECTATION": "Gallery should mirror Carbon stories with labeled buttons, disabled states, range slider, and all four DataTable variants.",
    "NEW INSTRUCTION": "WHEN updating gallery.py THEN mirror Carbon stories and include these specific examples"
}

[2026-04-05 13:21] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery completeness",
    "EXPECTATION": "Gallery should include labeled buttons, disabled variants, a range slider, and all four DataTable variants, aligning examples with Carbon Storybook.",
    "NEW INSTRUCTION": "WHEN updating gallery.py THEN mirror Carbon Storybook and include labels, disabled buttons, range slider, DataTable variants"
}

[2026-04-05 13:32] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Props coverage",
    "EXPECTATION": "Dash wrappers must expose all Carbon component props (e.g., Button.kind) using Carbon TS/TSX to determine required/optional and defaults.",
    "NEW INSTRUCTION": "WHEN generating wrappers THEN parse Carbon TS/TSX types and include all component props"
}

[2026-04-05 13:34] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Props coverage",
    "EXPECTATION": "All Carbon component props (e.g., Button.kind) must be exposed in Dash wrappers using Carbon TSX to determine required/optional and defaults.",
    "NEW INSTRUCTION": "WHEN generating wrappers THEN derive props from Carbon TS/TSX and include required/optional/defaults"
}

[2026-04-05 13:38] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery runtime error",
    "EXPECTATION": "Running gallery.py still triggers a JavaScript error; it needs to be fixed.",
    "NEW INSTRUCTION": "WHEN running gallery.py and console shows JS errors THEN reproduce, locate source, and fix"
}

[2026-04-05 13:39] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery runtime error",
    "EXPECTATION": "The gallery still throws a JavaScript error during runtime and needs to be fixed.",
    "NEW INSTRUCTION": "WHEN running gallery.py and console shows JS errors THEN reproduce issue, trace root cause, and fix"
}

[2026-04-05 13:39] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery runtime error",
    "EXPECTATION": "Identify and fix the JavaScript error occurring when running the gallery app from gallery.py.",
    "NEW INSTRUCTION": "WHEN running gallery.py THEN open browser console, capture JS error stack, and fix root cause"
}

[2026-04-05 13:41] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery runtime error",
    "EXPECTATION": "There is a JavaScript error when running gallery.py; it must be identified and fixed.",
    "NEW INSTRUCTION": "WHEN running gallery.py THEN open console, capture error stack, trace offending code, and fix"
}

[2026-04-05 13:41] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery runtime error",
    "EXPECTATION": "There is a JavaScript error when running gallery.py; it should be reproduced via the browser console and fixed.",
    "NEW INSTRUCTION": "WHEN running gallery.py and UI misbehaves THEN open console, capture stack, and fix"
}

[2026-04-05 13:42] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery runtime error",
    "EXPECTATION": "The gallery should run without JavaScript console errors; identify and fix the current issue.",
    "NEW INSTRUCTION": "WHEN running gallery.py and browser shows JS errors THEN capture error stack, locate offending code, and fix"
}

[2026-04-05 13:42] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery runtime error",
    "EXPECTATION": "Identify and fix the JavaScript error occurring when running gallery.py so the gallery runs without console errors.",
    "NEW INSTRUCTION": "WHEN running gallery.py and console shows JS errors THEN capture stack trace and fix offending code"
}

[2026-04-05 13:43] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery runtime error",
    "EXPECTATION": "The gallery should run without JavaScript console errors; identify and fix the current issue.",
    "NEW INSTRUCTION": "WHEN running gallery.py and console shows JS errors THEN capture stack trace and fix offending code"
}

[2026-04-05 13:44] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Scope and coverage",
    "EXPECTATION": "Automation must achieve full coverage of @carbon/react and avoid gaps or undefined components.",
    "NEW INSTRUCTION": "WHEN running generation pipeline THEN compare to @carbon/react exports and fail on missing wrappers"
}

[2026-04-05 13:47] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Scope and coverage",
    "EXPECTATION": "Automation should achieve full coverage of @carbon/react without omissions or regressions.",
    "NEW INSTRUCTION": "WHEN concluding a generation pass THEN output coverage report vs @carbon/react and fix gaps"
}

[2026-04-05 13:48] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Scope and coverage",
    "EXPECTATION": "Ensure full, verified coverage of all @carbon/react components and avoid omissions.",
    "NEW INSTRUCTION": "WHEN running generation pipeline THEN diff @carbon/react exports and fail build on gaps"
}

[2026-04-05 13:48] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Scope and coverage",
    "EXPECTATION": "Achieve full automated coverage of @carbon/react and be careful to avoid omissions.",
    "NEW INSTRUCTION": "WHEN concluding a generation pass THEN diff against @carbon/react exports and fail on gaps"
}

[2026-04-05 13:50] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Lib components inclusion",
    "EXPECTATION": "Automation should capture components directly from @carbon/react/lib (not only main exports) so ChatButton and similar are exposed on the Dash side.",
    "NEW INSTRUCTION": "WHEN generating wrappers THEN discover @carbon/react/lib/components/* and generate/expose wrappers"
}

[2026-04-05 13:51] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Lib components inclusion",
    "EXPECTATION": "Capture components directly from @carbon/react/lib so ChatButton and similar are exposed on the Dash side.",
    "NEW INSTRUCTION": "WHEN generating wrappers THEN discover @carbon/react/lib/components/* and generate/expose wrappers"
}

[2026-04-05 13:53] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Inclusion criteria",
    "EXPECTATION": "Only include components officially exported by @carbon/react; exclude lib-only items from wrappers and the gallery.",
    "NEW INSTRUCTION": "WHEN discovering component not exported by @carbon/react THEN exclude it from wrappers and gallery"
}

[2026-04-05 13:55] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Inclusion criteria",
    "EXPECTATION": "Only components exported by @carbon/react should be generated and shown in the gallery; lib-only items must be excluded.",
    "NEW INSTRUCTION": "WHEN a component is not exported by @carbon/react THEN exclude from wrappers and gallery"
}

[2026-04-05 13:55] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Inclusion criteria",
    "EXPECTATION": "Only include components exported by @carbon/react; exclude lib-only items from wrappers and the gallery.",
    "NEW INSTRUCTION": "WHEN discovering component not exported by @carbon/react THEN exclude from wrappers and gallery"
}

[2026-04-05 13:56] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Inclusion criteria enforcement",
    "EXPECTATION": "Only components exported by @carbon/react should appear in wrappers and the gallery; lib-only items must be excluded.",
    "NEW INSTRUCTION": "WHEN a component is not exported by @carbon/react THEN exclude from wrappers and gallery"
}

[2026-04-05 13:56] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Inclusion criteria enforcement",
    "EXPECTATION": "Only components exported by @carbon/react should appear; lib-only items must be excluded from wrappers and the gallery.",
    "NEW INSTRUCTION": "WHEN a component is not exported by @carbon/react THEN exclude from wrappers and gallery"
}

[2026-04-05 14:20] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery completeness",
    "EXPECTATION": "The Button gallery should mirror Carbon stories, including Icon-only (IconButton) and ButtonSkeleton variants.",
    "NEW INSTRUCTION": "WHEN mirroring Carbon Button stories THEN include icon-only and ButtonSkeleton examples"
}

[2026-04-05 14:21] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery completeness",
    "EXPECTATION": "Button stories should include Icon-only (IconButton) and ButtonSkeleton variants as in Carbon Storybook.",
    "NEW INSTRUCTION": "WHEN mirroring Carbon Button stories THEN include icon-only and ButtonSkeleton examples"
}

[2026-04-05 14:27] - Updated by Junie
{
    "TYPE": "preference",
    "CATEGORY": "Stories-driven gallery",
    "EXPECTATION": "Use the provided Carbon Storybook stories content to construct the gallery/examples automatically.",
    "NEW INSTRUCTION": "WHEN generating or updating gallery examples THEN mirror Carbon Storybook stories content provided"
}

[2026-04-05 14:38] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Button kind not applied",
    "EXPECTATION": "The Button.kind prop must be accepted and forwarded so variants render correctly instead of all appearing primary.",
    "NEW INSTRUCTION": "WHEN generating Button wrapper THEN forward 'kind' prop to Carbon Button supporting all variants"
}

[2026-04-05 14:40] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Reserved props handling",
    "EXPECTATION": "Generated Python APIs must not use reserved keywords (e.g., 'as'); props should be aliased safely and back-mapped.",
    "NEW INSTRUCTION": "WHEN generating Python kwargs from TS props THEN alias reserved keywords (e.g., as->as_) and back-map"
}

[2026-04-05 14:42] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Reserved keyword aliasing",
    "EXPECTATION": "Generated Python APIs must not use reserved keywords like 'as'; use safe aliases and back-map to JS.",
    "NEW INSTRUCTION": "WHEN generating Python kwargs from TS props THEN alias reserved keywords (e.g., as->as_) and back-map"
}

[2026-04-05 14:43] - Updated by Junie
{
    "TYPE": "preference",
    "CATEGORY": "Commit workflow",
    "EXPECTATION": "Create a git commit before making fixes or changes when addressing issues.",
    "NEW INSTRUCTION": "WHEN starting a fix THEN create a git commit of current state"
}

[2026-04-05 14:43] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Reserved keyword aliasing",
    "EXPECTATION": "Python APIs must not use reserved keywords; 'as' should be aliased (e.g., as_) and back-mapped to JS so generated usage like Grid(...) is valid.",
    "NEW INSTRUCTION": "WHEN generating Python kwargs from TS props THEN alias reserved keywords (e.g., as->as_) and back-map"
}

[2026-04-05 14:47] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Reserved keyword aliasing",
    "EXPECTATION": "Generated Python APIs must not use reserved keywords; use safe aliases like as_ and back-map to JS.",
    "NEW INSTRUCTION": "WHEN generating Python kwargs from TS props THEN alias reserved keywords (e.g., as->as_) and back-map"
}

[2026-04-05 14:47] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Reserved keyword aliasing",
    "EXPECTATION": "Python API should not use reserved keywords like 'as'; Grid should accept 'as_' and back-map to JS.",
    "NEW INSTRUCTION": "WHEN generating Python kwargs from TS props THEN alias reserved keywords (e.g., as->as_) and back-map"
}

[2026-04-05 14:51] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Automation vs. rewrites",
    "EXPECTATION": "Fix DataTable and DatePicker runtime issues by improving the generation/config scripts, not by rewriting the components.",
    "NEW INSTRUCTION": "WHEN a wrapped component errors due to missing internals THEN extend generation to import and wire required submodules"
}

[2026-04-05 14:54] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery console errors",
    "EXPECTATION": "Gallery should run without JS console errors/warnings; current defaultProps warnings persist from generated components.",
    "NEW INSTRUCTION": "WHEN generating React wrappers THEN replace defaultProps with JS default parameters"
}

[2026-04-05 14:56] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Automation-first fixes",
    "EXPECTATION": "Address issues by improving the generation/build scripts instead of patching individual components.",
    "NEW INSTRUCTION": "WHEN a component misbehaves THEN modify generation pipeline to fix root cause globally"
}

[2026-04-05 14:58] - Updated by Junie
{
    "TYPE": "preference",
    "CATEGORY": "Automation-first approach",
    "EXPECTATION": "Address problems by improving generation/build scripts rather than patching individual components.",
    "NEW INSTRUCTION": "WHEN encountering a component-specific issue THEN fix generation/build scripts to solve globally"
}

[2026-04-05 15:10] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "DefaultProps deprecation",
    "EXPECTATION": "Generated React components must avoid defaultProps and use JavaScript default parameters to prevent console warnings.",
    "NEW INSTRUCTION": "WHEN generating React wrappers THEN replace defaultProps with JS default parameters"
}

[2026-04-05 15:13] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "DefaultProps deprecation",
    "EXPECTATION": "Generated React wrappers (including async chunks) must not use defaultProps; use JS default parameters so no console warnings, similar to Dash Mantine.",
    "NEW INSTRUCTION": "WHEN generating React or async wrapper files THEN use default parameters, never defaultProps"
}

[2026-04-05 15:31] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Prop type mapping",
    "EXPECTATION": "Button.hasIconOnly should accept a boolean, not a ReactNode; generated props must match Carbon TS types.",
    "NEW INSTRUCTION": "WHEN deriving prop types from Carbon TSX THEN map boolean props to boolean, not node"
}

[2026-04-05 15:32] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Prop type mapping",
    "EXPECTATION": "Button.hasIconOnly should be a boolean prop per Carbon TSX, and the Dash wrapper must accept a boolean value.",
    "NEW INSTRUCTION": "WHEN deriving prop types from Carbon TS/TSX THEN map boolean props to boolean, not node"
}

[2026-04-05 15:33] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Prop type mapping",
    "EXPECTATION": "Button.hasIconOnly must be a boolean prop per Carbon TSX; passing true should be valid and not expect a ReactNode.",
    "NEW INSTRUCTION": "WHEN generating prop types from Carbon TS/TSX THEN map hasIconOnly to boolean"
}

[2026-04-05 15:37] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Icon prop handling",
    "EXPECTATION": "renderIcon should accept an icon component/function (e.g., DashIconify), not a string name.",
    "NEW INSTRUCTION": "WHEN a prop is renderIcon THEN accept ReactNode/function and reject string names"
}

[2026-04-05 15:38] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Icon prop handling",
    "EXPECTATION": "renderIcon should receive a component/function (e.g., DashIconify or a Carbon icon), not a string name.",
    "NEW INSTRUCTION": "WHEN a prop is renderIcon THEN accept ReactNode/function and reject string names"
}

[2026-04-05 15:40] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Controlled components",
    "EXPECTATION": "Generated components should not switch between uncontrolled and controlled; choose one approach consistently.",
    "NEW INSTRUCTION": "WHEN generating props value/checked/selected THEN use controlled pattern with explicit safe defaults"
}

[2026-04-05 15:40] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Controlled/uncontrolled warning",
    "EXPECTATION": "Components must not switch between uncontrolled and controlled; keep value-like props controlled for lifetime.",
    "NEW INSTRUCTION": "WHEN component has value/checked/selected props THEN use controlled pattern, set safe defaults, never pass undefined to Carbon"
}

[2026-04-05 15:43] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Controlled components",
    "EXPECTATION": "Components must not switch between uncontrolled and controlled; keep value-like props controlled for lifetime.",
    "NEW INSTRUCTION": "WHEN component has value/checked/selected props THEN use controlled pattern, set safe defaults"
}

[2026-04-05 15:44] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Controlled components",
    "EXPECTATION": "Components must not switch from uncontrolled to controlled; keep value-like props controlled with safe defaults.",
    "NEW INSTRUCTION": "WHEN component has value/checked/selected props THEN use controlled pattern and never pass undefined"
}

[2026-04-05 15:45] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Controlled components warning",
    "EXPECTATION": "Value-like props must remain controlled for the component’s lifetime; avoid undefined-to-defined transitions.",
    "NEW INSTRUCTION": "WHEN generating wrappers with value-like props THEN use controlled defaults and never pass undefined"
}

[2026-04-06 10:11] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Prop value misuse",
    "EXPECTATION": "TreeView.active must be a boolean; do not pass string IDs to boolean props. Use the correct selection/ID prop per Carbon stories.",
    "NEW INSTRUCTION": "WHEN updating TreeView gallery/example THEN set active to boolean and use the ID selection prop"
}

[2026-04-06 10:14] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Prop typing exceptions",
    "EXPECTATION": "Keep 'active' as a boolean where appropriate and maintain a specific exceptions list for components that require different types, to improve broad component coverage.",
    "NEW INSTRUCTION": "WHEN generating prop types THEN default 'active' to boolean and apply per-component overrides"
}

[2026-04-06 10:22] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Story-driven tests",
    "EXPECTATION": "Add tests for DataTable and Tabs derived from Carbon Storybook stories to catch current render failures.",
    "NEW INSTRUCTION": "WHEN creating component tests THEN derive scenarios from Carbon Storybook stories"
}

[2026-04-06 10:38] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "JS error capture",
    "EXPECTATION": "Capture JavaScript console errors by running the app with debug disabled and inspecting a real browser console; curl cannot capture JS errors.",
    "NEW INSTRUCTION": "WHEN checking for frontend JS errors THEN run app with debug=False and capture browser console logs"
}

[2026-04-06 10:41] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "JS error capture",
    "EXPECTATION": "Use a real browser console with the app running in debug=False to capture frontend JS errors; curl cannot capture JS errors.",
    "NEW INSTRUCTION": "WHEN checking for frontend JS errors THEN run app with debug=False and capture browser console logs"
}

[2026-04-06 10:53] - Updated by Junie
{
    "TYPE": "correction",
    "CATEGORY": "Gallery render failure",
    "EXPECTATION": "DataTable should render and be visible in the gallery/examples.",
    "NEW INSTRUCTION": "WHEN DataTable not rendering in gallery THEN capture browser console errors and fix via generation pipeline"
}

