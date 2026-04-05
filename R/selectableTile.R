# AUTO GENERATED FILE - DO NOT EDIT

#' @export
selectableTile <- function(children=NULL, id=NULL, className=NULL, debounce=NULL, decorator=NULL, disabled=NULL, hasRoundedCorners=NULL, light=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, name=NULL, onChange=NULL, onClick=NULL, onKeyDown=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, selected=NULL, slug=NULL, style=NULL, tabIndex=NULL, title=NULL, value=NULL) {
    
    props <- list(children=children, id=id, className=className, debounce=debounce, decorator=decorator, disabled=disabled, hasRoundedCorners=hasRoundedCorners, light=light, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, name=name, onChange=onChange, onClick=onClick, onKeyDown=onKeyDown, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, selected=selected, slug=slug, style=style, tabIndex=tabIndex, title=title, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SelectableTile',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'debounce', 'decorator', 'disabled', 'hasRoundedCorners', 'light', 'loading_state', 'n_blur', 'n_submit', 'name', 'onChange', 'onClick', 'onKeyDown', 'persisted_props', 'persistence', 'persistence_type', 'selected', 'slug', 'style', 'tabIndex', 'title', 'value'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
