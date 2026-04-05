# AUTO GENERATED FILE - DO NOT EDIT

#' @export
progressBar <- function(children=NULL, id=NULL, className=NULL, debounce=NULL, helperText=NULL, hideLabel=NULL, label=NULL, loading_state=NULL, max=NULL, n_blur=NULL, n_submit=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, size=NULL, status=NULL, style=NULL, type=NULL, value=NULL) {
    
    props <- list(children=children, id=id, className=className, debounce=debounce, helperText=helperText, hideLabel=hideLabel, label=label, loading_state=loading_state, max=max, n_blur=n_blur, n_submit=n_submit, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, size=size, status=status, style=style, type=type, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ProgressBar',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'debounce', 'helperText', 'hideLabel', 'label', 'loading_state', 'max', 'n_blur', 'n_submit', 'persisted_props', 'persistence', 'persistence_type', 'size', 'status', 'style', 'type', 'value'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
