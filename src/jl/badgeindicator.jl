# AUTO GENERATED FILE - DO NOT EDIT

export badgeindicator

"""
    badgeindicator(;kwargs...)
    badgeindicator(children::Any;kwargs...)
    badgeindicator(children_maker::Function;kwargs...)


A BadgeIndicator component.
BadgeIndicator is a wrapper for the Carbon BadgeIndicator component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function badgeindicator(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("badgeindicator", "BadgeIndicator", "carbon_dash", available_props, wild_props; kwargs...)
end

badgeindicator(children::Any; kwargs...) = badgeindicator(;kwargs..., children = children)
badgeindicator(children_maker::Function; kwargs...) = badgeindicator(children_maker(); kwargs...)

