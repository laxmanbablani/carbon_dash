# AUTO GENERATED FILE - DO NOT EDIT

export treenode

"""
    treenode(;kwargs...)
    treenode(children::Any;kwargs...)
    treenode(children_maker::Function;kwargs...)


A TreeNode component.
TreeNode is a wrapper for the Carbon TreeNode component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `active` (Bool | Real | String | Dict | Array; optional): active
- `align` (Bool | Real | String | Dict | Array; optional): align
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `defaultIsExpanded` (Bool | Real | String | Dict | Array; optional): defaultIsExpanded
- `depth` (Bool | Real | String | Dict | Array; optional): depth
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `href` (Bool | Real | String | Dict | Array; optional): href
- `isExpanded` (Bool | Real | String | Dict | Array; optional): isExpanded
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `onNodeFocusEvent` (Bool | Real | String | Dict | Array; optional): onNodeFocusEvent
- `onSelect` (Bool | Real | String | Dict | Array; optional): onSelect
- `onToggle` (Bool | Real | String | Dict | Array; optional): onToggle
- `onTreeSelect` (Bool | Real | String | Dict | Array; optional): onTreeSelect
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `selected` (Bool | Real | String | Dict | Array; optional): selected
- `style` (Dict; optional): style
- `value` (Bool | Real | String | Dict | Array; optional): value
"""
function treenode(; kwargs...)
        available_props = Symbol[:children, :id, :active, :align, :autoAlign, :className, :debounce, :defaultIsExpanded, :depth, :disabled, :href, :isExpanded, :label, :loading_state, :n_blur, :n_submit, :onNodeFocusEvent, :onSelect, :onToggle, :onTreeSelect, :persisted_props, :persistence, :persistence_type, :renderIcon, :selected, :style, :value]
        wild_props = Symbol[]
        return Component("treenode", "TreeNode", "carbon_dash", available_props, wild_props; kwargs...)
end

treenode(children::Any; kwargs...) = treenode(;kwargs..., children = children)
treenode(children_maker::Function; kwargs...) = treenode(children_maker(); kwargs...)

