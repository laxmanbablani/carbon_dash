# AUTO GENERATED FILE - DO NOT EDIT

export disclosure

"""
    disclosure(;kwargs...)
    disclosure(children::Any;kwargs...)
    disclosure(children_maker::Function;kwargs...)


A Disclosure component.
Disclosure is a wrapper for the Carbon Disclosure component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function disclosure(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("disclosure", "Disclosure", "carbon_dash", available_props, wild_props; kwargs...)
end

disclosure(children::Any; kwargs...) = disclosure(;kwargs..., children = children)
disclosure(children_maker::Function; kwargs...) = disclosure(children_maker(); kwargs...)

