# AUTO GENERATED FILE - DO NOT EDIT

export chatbutton

"""
    chatbutton(;kwargs...)
    chatbutton(children::Any;kwargs...)
    chatbutton(children_maker::Function;kwargs...)


A ChatButton component.
ChatButton is a wrapper for the Carbon ChatButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `isQuickAction` (Bool | Real | String | Dict | Array; optional): isQuickAction
- `isSelected` (Bool | Real | String | Dict | Array; optional): isSelected
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `renderIcon` (a list of or a singular dash component, string or number; optional): renderIcon
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function chatbutton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :disabled, :isQuickAction, :isSelected, :kind, :loading_state, :renderIcon, :size, :style]
        wild_props = Symbol[]
        return Component("chatbutton", "ChatButton", "carbon_dash", available_props, wild_props; kwargs...)
end

chatbutton(children::Any; kwargs...) = chatbutton(;kwargs..., children = children)
chatbutton(children_maker::Function; kwargs...) = chatbutton(children_maker(); kwargs...)

