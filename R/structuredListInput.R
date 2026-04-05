# AUTO GENERATED FILE - DO NOT EDIT

#' @export
structuredListInput <- function(children=NULL, id=NULL, className=NULL, debounce=NULL, defaultChecked=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, name=NULL, onChange=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, style=NULL, title=NULL, value=NULL) {
    
    props <- list(children=children, id=id, className=className, debounce=debounce, defaultChecked=defaultChecked, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, name=name, onChange=onChange, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, style=style, title=title, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'StructuredListInput',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'debounce', 'defaultChecked', 'loading_state', 'n_blur', 'n_submit', 'name', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'style', 'title', 'value'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
