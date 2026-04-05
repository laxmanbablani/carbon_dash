# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableSelectAll <- function(children=NULL, id=NULL, ariaLabel=NULL, checked=NULL, className=NULL, debounce=NULL, disabled=NULL, indeterminate=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, name=NULL, onSelect=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, style=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, checked=checked, className=className, debounce=debounce, disabled=disabled, indeterminate=indeterminate, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, name=name, onSelect=onSelect, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableSelectAll',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'checked', 'className', 'debounce', 'disabled', 'indeterminate', 'loading_state', 'n_blur', 'n_submit', 'name', 'onSelect', 'persisted_props', 'persistence', 'persistence_type', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
