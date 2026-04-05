# AUTO GENERATED FILE - DO NOT EDIT

export iconbuttonkinds

"""
    iconbuttonkinds(;kwargs...)
    iconbuttonkinds(children::Any;kwargs...)
    iconbuttonkinds(children_maker::Function;kwargs...)


An IconButtonKinds component.
IconButtonKinds is a wrapper for the Carbon IconButtonKinds component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
- `style` (Dict; optional): Inline styles
"""
function iconbuttonkinds(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style]
        wild_props = Symbol[]
        return Component("iconbuttonkinds", "IconButtonKinds", "carbon_dash", available_props, wild_props; kwargs...)
end

iconbuttonkinds(children::Any; kwargs...) = iconbuttonkinds(;kwargs..., children = children)
iconbuttonkinds(children_maker::Function; kwargs...) = iconbuttonkinds(children_maker(); kwargs...)

