# AUTO GENERATED FILE - DO NOT EDIT

#' @export
treeNode <- function(children=NULL, id=NULL, active=NULL, align=NULL, autoAlign=NULL, className=NULL, debounce=NULL, defaultIsExpanded=NULL, depth=NULL, disabled=NULL, href=NULL, isExpanded=NULL, label=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, onNodeFocusEvent=NULL, onSelect=NULL, onToggle=NULL, onTreeSelect=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, renderIcon=NULL, selected=NULL, style=NULL, value=NULL) {
    
    props <- list(children=children, id=id, active=active, align=align, autoAlign=autoAlign, className=className, debounce=debounce, defaultIsExpanded=defaultIsExpanded, depth=depth, disabled=disabled, href=href, isExpanded=isExpanded, label=label, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, onNodeFocusEvent=onNodeFocusEvent, onSelect=onSelect, onToggle=onToggle, onTreeSelect=onTreeSelect, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, renderIcon=renderIcon, selected=selected, style=style, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TreeNode',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'active', 'align', 'autoAlign', 'className', 'debounce', 'defaultIsExpanded', 'depth', 'disabled', 'href', 'isExpanded', 'label', 'loading_state', 'n_blur', 'n_submit', 'onNodeFocusEvent', 'onSelect', 'onToggle', 'onTreeSelect', 'persisted_props', 'persistence', 'persistence_type', 'renderIcon', 'selected', 'style', 'value'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
