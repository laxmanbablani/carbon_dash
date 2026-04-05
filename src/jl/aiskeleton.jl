# AUTO GENERATED FILE - DO NOT EDIT

export aiskeleton

"""
    aiskeleton(;kwargs...)
    aiskeleton(children::Any;kwargs...)
    aiskeleton(children_maker::Function;kwargs...)


An AISkeleton component.
AISkeleton is a wrapper for the Carbon AISkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function aiskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("aiskeleton", "AISkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

aiskeleton(children::Any; kwargs...) = aiskeleton(;kwargs..., children = children)
aiskeleton(children_maker::Function; kwargs...) = aiskeleton(children_maker(); kwargs...)

