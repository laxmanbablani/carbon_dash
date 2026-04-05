# AUTO GENERATED FILE - DO NOT EDIT

export portal

"""
    portal(;kwargs...)
    portal(children::Any;kwargs...)
    portal(children_maker::Function;kwargs...)


A Portal component.
Portal is a wrapper for the Carbon Portal component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function portal(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("portal", "Portal", "carbon_dash", available_props, wild_props; kwargs...)
end

portal(children::Any; kwargs...) = portal(;kwargs..., children = children)
portal(children_maker::Function; kwargs...) = portal(children_maker(); kwargs...)

