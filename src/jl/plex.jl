# AUTO GENERATED FILE - DO NOT EDIT

export plex

"""
    plex(;kwargs...)
    plex(children::Any;kwargs...)
    plex(children_maker::Function;kwargs...)


A Plex component.
Plex is a wrapper for the Carbon Plex component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function plex(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("plex", "Plex", "carbon_dash", available_props, wild_props; kwargs...)
end

plex(children::Any; kwargs...) = plex(;kwargs..., children = children)
plex(children_maker::Function; kwargs...) = plex(children_maker(); kwargs...)

