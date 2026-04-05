# AUTO GENERATED FILE - DO NOT EDIT

export togglesmall

"""
    togglesmall(;kwargs...)
    togglesmall(children::Any;kwargs...)
    togglesmall(children_maker::Function;kwargs...)


A ToggleSmall component.
ToggleSmall is a wrapper for the Carbon ToggleSmall component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function togglesmall(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("togglesmall", "ToggleSmall", "carbon_dash", available_props, wild_props; kwargs...)
end

togglesmall(children::Any; kwargs...) = togglesmall(;kwargs..., children = children)
togglesmall(children_maker::Function; kwargs...) = togglesmall(children_maker(); kwargs...)

