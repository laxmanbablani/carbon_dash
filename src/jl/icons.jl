# AUTO GENERATED FILE - DO NOT EDIT

export icons

"""
    icons(;kwargs...)
    icons(children::Any;kwargs...)
    icons(children_maker::Function;kwargs...)


An Icons component.
Icons is a wrapper for the Carbon Icons component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function icons(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("icons", "Icons", "carbon_dash", available_props, wild_props; kwargs...)
end

icons(children::Any; kwargs...) = icons(;kwargs..., children = children)
icons(children_maker::Function; kwargs...) = icons(children_maker(); kwargs...)

