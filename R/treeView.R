# AUTO GENERATED FILE - DO NOT EDIT

#' @export
treeView <- function(children=NULL, id=NULL, active=NULL, className=NULL, hideLabel=NULL, label=NULL, loading_state=NULL, multiselect=NULL, onActivate=NULL, onSelect=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, selected=NULL, size=NULL, style=NULL) {
    
    props <- list(children=children, id=id, active=active, className=className, hideLabel=hideLabel, label=label, loading_state=loading_state, multiselect=multiselect, onActivate=onActivate, onSelect=onSelect, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, selected=selected, size=size, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TreeView',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'active', 'className', 'hideLabel', 'label', 'loading_state', 'multiselect', 'onActivate', 'onSelect', 'persisted_props', 'persistence', 'persistence_type', 'selected', 'size', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
