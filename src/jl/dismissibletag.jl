# AUTO GENERATED FILE - DO NOT EDIT

export dismissibletag

"""
    dismissibletag(;kwargs...)
    dismissibletag(children::Any;kwargs...)
    dismissibletag(children_maker::Function;kwargs...)


A DismissibleTag component.
DismissibleTag is a wrapper for the Carbon DismissibleTag component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `dismissTooltipAlignment` (Bool | Real | String | Dict | Array; optional): dismissTooltipAlignment
- `dismissTooltipLabel` (Bool | Real | String | Dict | Array; optional): dismissTooltipLabel
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClose` (Bool | Real | String | Dict | Array; optional): onClose
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `tagTitle` (Bool | Real | String | Dict | Array; optional): tagTitle
- `text` (Bool | Real | String | Dict | Array; optional): text
- `title` (Bool | Real | String | Dict | Array; optional): title
- `type` (Bool | Real | String | Dict | Array; optional): type
"""
function dismissibletag(; kwargs...)
        available_props = Symbol[:children, :id, :className, :decorator, :disabled, :dismissTooltipAlignment, :dismissTooltipLabel, :loading_state, :onClose, :renderIcon, :size, :slug, :style, :tagTitle, :text, :title, :type]
        wild_props = Symbol[]
        return Component("dismissibletag", "DismissibleTag", "carbon_dash", available_props, wild_props; kwargs...)
end

dismissibletag(children::Any; kwargs...) = dismissibletag(;kwargs..., children = children)
dismissibletag(children_maker::Function; kwargs...) = dismissibletag(children_maker(); kwargs...)

