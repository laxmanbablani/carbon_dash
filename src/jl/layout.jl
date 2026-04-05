# AUTO GENERATED FILE - DO NOT EDIT

export layout

"""
    layout(;kwargs...)
    layout(children::Any;kwargs...)
    layout(children_maker::Function;kwargs...)


A Layout component.
Layout is a wrapper for the Carbon Layout component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function layout(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("layout", "Layout", "carbon_dash", available_props, wild_props; kwargs...)
end

layout(children::Any; kwargs...) = layout(;kwargs..., children = children)
layout(children_maker::Function; kwargs...) = layout(children_maker(); kwargs...)

