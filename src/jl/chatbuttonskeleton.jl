# AUTO GENERATED FILE - DO NOT EDIT

export chatbuttonskeleton

"""
    chatbuttonskeleton(;kwargs...)
    chatbuttonskeleton(children::Any;kwargs...)
    chatbuttonskeleton(children_maker::Function;kwargs...)


A ChatButtonSkeleton component.
ChatButtonSkeleton is a wrapper for the Carbon ChatButtonSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function chatbuttonskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :size, :style]
        wild_props = Symbol[]
        return Component("chatbuttonskeleton", "ChatButtonSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

chatbuttonskeleton(children::Any; kwargs...) = chatbuttonskeleton(;kwargs..., children = children)
chatbuttonskeleton(children_maker::Function; kwargs...) = chatbuttonskeleton(children_maker(); kwargs...)

