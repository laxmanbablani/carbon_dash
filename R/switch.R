# AUTO GENERATED FILE - DO NOT EDIT

#' @export
switch <- function(children=NULL, id=NULL, className=NULL, disabled=NULL, index=NULL, loading_state=NULL, name=NULL, onClick=NULL, onKeyDown=NULL, selected=NULL, style=NULL, text=NULL) {
    
    props <- list(children=children, id=id, className=className, disabled=disabled, index=index, loading_state=loading_state, name=name, onClick=onClick, onKeyDown=onKeyDown, selected=selected, style=style, text=text)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Switch',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'disabled', 'index', 'loading_state', 'name', 'onClick', 'onKeyDown', 'selected', 'style', 'text'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
