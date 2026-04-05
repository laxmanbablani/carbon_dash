# AUTO GENERATED FILE - DO NOT EDIT

export layoutdirection

"""
    layoutdirection(;kwargs...)
    layoutdirection(children::Any;kwargs...)
    layoutdirection(children_maker::Function;kwargs...)


A LayoutDirection component.
LayoutDirection is a wrapper for the Carbon LayoutDirection component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function layoutdirection(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("layoutdirection", "LayoutDirection", "carbon_dash", available_props, wild_props; kwargs...)
end

layoutdirection(children::Any; kwargs...) = layoutdirection(;kwargs..., children = children)
layoutdirection(children_maker::Function; kwargs...) = layoutdirection(children_maker(); kwargs...)

