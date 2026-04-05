# AUTO GENERATED FILE - DO NOT EDIT

export structuredlist

"""
    structuredlist(;kwargs...)
    structuredlist(children::Any;kwargs...)
    structuredlist(children_maker::Function;kwargs...)


A StructuredList component.
StructuredList is a wrapper for the Carbon StructuredList component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function structuredlist(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("structuredlist", "StructuredList", "carbon_dash", available_props, wild_props; kwargs...)
end

structuredlist(children::Any; kwargs...) = structuredlist(;kwargs..., children = children)
structuredlist(children_maker::Function; kwargs...) = structuredlist(children_maker(); kwargs...)

