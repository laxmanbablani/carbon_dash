# AUTO GENERATED FILE - DO NOT EDIT

#' @export
selectItem <- function(children=NULL, id=NULL, className=NULL, debounce=NULL, disabled=NULL, hidden=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, style=NULL, text=NULL, value=NULL) {
    
    props <- list(children=children, id=id, className=className, debounce=debounce, disabled=disabled, hidden=hidden, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, style=style, text=text, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SelectItem',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'debounce', 'disabled', 'hidden', 'loading_state', 'n_blur', 'n_submit', 'persisted_props', 'persistence', 'persistence_type', 'style', 'text', 'value'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
