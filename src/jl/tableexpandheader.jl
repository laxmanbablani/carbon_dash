# AUTO GENERATED FILE - DO NOT EDIT

export tableexpandheader

"""
    tableexpandheader(;kwargs...)
    tableexpandheader(children::Any;kwargs...)
    tableexpandheader(children_maker::Function;kwargs...)


A TableExpandHeader component.
TableExpandHeader is a wrapper for the Carbon TableExpandHeader component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `className` (String; optional): className
- `enableExpando` (Bool | Real | String | Dict | Array; optional): enableExpando
- `enableToggle` (Bool | Real | String | Dict | Array; optional): enableToggle
- `expandIconDescription` (Bool | Real | String | Dict | Array; optional): expandIconDescription
- `isExpanded` (Bool; optional): isExpanded
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onExpand` (Bool | Real | String | Dict | Array; optional): onExpand
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `style` (Dict; optional): style
"""
function tableexpandheader(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :className, :enableExpando, :enableToggle, :expandIconDescription, :isExpanded, :loading_state, :onExpand, :persisted_props, :persistence, :persistence_type, :style]
        wild_props = Symbol[]
        return Component("tableexpandheader", "TableExpandHeader", "carbon_dash", available_props, wild_props; kwargs...)
end

tableexpandheader(children::Any; kwargs...) = tableexpandheader(;kwargs..., children = children)
tableexpandheader(children_maker::Function; kwargs...) = tableexpandheader(children_maker(); kwargs...)

