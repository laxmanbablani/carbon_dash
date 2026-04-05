# AUTO GENERATED FILE - DO NOT EDIT

export icon

"""
    icon(;kwargs...)
    icon(children::Any;kwargs...)
    icon(children_maker::Function;kwargs...)


An Icon component.
Icon is a wrapper for the Carbon Icon component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function icon(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("icon", "Icon", "carbon_dash", available_props, wild_props; kwargs...)
end

icon(children::Any; kwargs...) = icon(;kwargs..., children = children)
icon(children_maker::Function; kwargs...) = icon(children_maker(); kwargs...)

