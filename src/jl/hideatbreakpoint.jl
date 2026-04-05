# AUTO GENERATED FILE - DO NOT EDIT

export hideatbreakpoint

"""
    hideatbreakpoint(;kwargs...)
    hideatbreakpoint(children::Any;kwargs...)
    hideatbreakpoint(children_maker::Function;kwargs...)


A HideAtBreakpoint component.
HideAtBreakpoint is a wrapper for the Carbon HideAtBreakpoint component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function hideatbreakpoint(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("hideatbreakpoint", "HideAtBreakpoint", "carbon_dash", available_props, wild_props; kwargs...)
end

hideatbreakpoint(children::Any; kwargs...) = hideatbreakpoint(;kwargs..., children = children)
hideatbreakpoint(children_maker::Function; kwargs...) = hideatbreakpoint(children_maker(); kwargs...)

