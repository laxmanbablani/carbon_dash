# AUTO GENERATED FILE - DO NOT EDIT

export overflowmenuitem

"""
    overflowmenuitem(;kwargs...)
    overflowmenuitem(children::Any;kwargs...)
    overflowmenuitem(children_maker::Function;kwargs...)


An OverflowMenuItem component.
OverflowMenuItem is a wrapper for the Carbon OverflowMenuItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `closeMenu` (Bool | Real | String | Dict | Array; optional): closeMenu
- `dangerDescription` (Bool | Real | String | Dict | Array; optional): dangerDescription
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `handleOverflowMenuItemFocus` (Bool | Real | String | Dict | Array; optional): handleOverflowMenuItemFocus
- `hasDivider` (Bool | Real | String | Dict | Array; optional): hasDivider
- `href` (Bool | Real | String | Dict | Array; optional): href
- `index` (Bool | Real | String | Dict | Array; optional): index
- `isDelete` (Bool | Real | String | Dict | Array; optional): isDelete
- `itemText` (Bool | Real | String | Dict | Array; optional): itemText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onBlur` (Bool | Real | String | Dict | Array; optional): onBlur
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onFocus` (Bool | Real | String | Dict | Array; optional): onFocus
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `onKeyUp` (Bool | Real | String | Dict | Array; optional): onKeyUp
- `onMouseDown` (Bool | Real | String | Dict | Array; optional): onMouseDown
- `onMouseEnter` (Bool | Real | String | Dict | Array; optional): onMouseEnter
- `onMouseLeave` (Bool | Real | String | Dict | Array; optional): onMouseLeave
- `onMouseUp` (Bool | Real | String | Dict | Array; optional): onMouseUp
- `requireTitle` (Bool | Real | String | Dict | Array; optional): requireTitle
- `style` (Dict; optional): style
- `title` (Bool | Real | String | Dict | Array; optional): title
- `wrapperClassName` (Bool | Real | String | Dict | Array; optional): wrapperClassName
"""
function overflowmenuitem(; kwargs...)
        available_props = Symbol[:children, :id, :className, :closeMenu, :dangerDescription, :disabled, :handleOverflowMenuItemFocus, :hasDivider, :href, :index, :isDelete, :itemText, :loading_state, :onBlur, :onClick, :onFocus, :onKeyDown, :onKeyUp, :onMouseDown, :onMouseEnter, :onMouseLeave, :onMouseUp, :requireTitle, :style, :title, :wrapperClassName]
        wild_props = Symbol[]
        return Component("overflowmenuitem", "OverflowMenuItem", "carbon_dash", available_props, wild_props; kwargs...)
end

overflowmenuitem(children::Any; kwargs...) = overflowmenuitem(;kwargs..., children = children)
overflowmenuitem(children_maker::Function; kwargs...) = overflowmenuitem(children_maker(); kwargs...)

