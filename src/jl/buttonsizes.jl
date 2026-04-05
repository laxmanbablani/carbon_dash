# AUTO GENERATED FILE - DO NOT EDIT

export buttonsizes

"""
    buttonsizes(;kwargs...)
    buttonsizes(children::Any;kwargs...)
    buttonsizes(children_maker::Function;kwargs...)


A ButtonSizes component.
ButtonSizes is a wrapper for the Carbon ButtonSizes component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
- `style` (Dict; optional): Inline styles
"""
function buttonsizes(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style]
        wild_props = Symbol[]
        return Component("buttonsizes", "ButtonSizes", "carbon_dash", available_props, wild_props; kwargs...)
end

buttonsizes(children::Any; kwargs...) = buttonsizes(;kwargs..., children = children)
buttonsizes(children_maker::Function; kwargs...) = buttonsizes(children_maker(); kwargs...)

