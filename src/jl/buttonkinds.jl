# AUTO GENERATED FILE - DO NOT EDIT

export buttonkinds

"""
    buttonkinds(;kwargs...)
    buttonkinds(children::Any;kwargs...)
    buttonkinds(children_maker::Function;kwargs...)


A ButtonKinds component.
ButtonKinds is a wrapper for the Carbon ButtonKinds component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
- `style` (Dict; optional): Inline styles
"""
function buttonkinds(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style]
        wild_props = Symbol[]
        return Component("buttonkinds", "ButtonKinds", "carbon_dash", available_props, wild_props; kwargs...)
end

buttonkinds(children::Any; kwargs...) = buttonkinds(;kwargs..., children = children)
buttonkinds(children_maker::Function; kwargs...) = buttonkinds(children_maker(); kwargs...)

