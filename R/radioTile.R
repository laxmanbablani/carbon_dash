# AUTO GENERATED FILE - DO NOT EDIT

#' @export
radioTile <- function(children=NULL, id=NULL, checked=NULL, className=NULL, debounce=NULL, decorator=NULL, disabled=NULL, hasRoundedCorners=NULL, light=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, name=NULL, onChange=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, required=NULL, slug=NULL, style=NULL, tabIndex=NULL, value=NULL) {
    
    props <- list(children=children, id=id, checked=checked, className=className, debounce=debounce, decorator=decorator, disabled=disabled, hasRoundedCorners=hasRoundedCorners, light=light, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, name=name, onChange=onChange, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, required=required, slug=slug, style=style, tabIndex=tabIndex, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'RadioTile',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'checked', 'className', 'debounce', 'decorator', 'disabled', 'hasRoundedCorners', 'light', 'loading_state', 'n_blur', 'n_submit', 'name', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'required', 'slug', 'style', 'tabIndex', 'value'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
