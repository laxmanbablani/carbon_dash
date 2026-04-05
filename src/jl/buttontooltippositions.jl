# AUTO GENERATED FILE - DO NOT EDIT

export buttontooltippositions

"""
    buttontooltippositions(;kwargs...)
    buttontooltippositions(children::Any;kwargs...)
    buttontooltippositions(children_maker::Function;kwargs...)


A ButtonTooltipPositions component.
ButtonTooltipPositions is a wrapper for the Carbon ButtonTooltipPositions component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
- `style` (Dict; optional): Inline styles
"""
function buttontooltippositions(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style]
        wild_props = Symbol[]
        return Component("buttontooltippositions", "ButtonTooltipPositions", "carbon_dash", available_props, wild_props; kwargs...)
end

buttontooltippositions(children::Any; kwargs...) = buttontooltippositions(;kwargs..., children = children)
buttontooltippositions(children_maker::Function; kwargs...) = buttontooltippositions(children_maker(); kwargs...)

