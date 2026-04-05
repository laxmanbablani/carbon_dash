# AUTO GENERATED FILE - DO NOT EDIT

#' @export
selectableTag <- function(children=NULL, id=NULL, className=NULL, defaultSelected=NULL, disabled=NULL, loading_state=NULL, onChange=NULL, onClick=NULL, renderIcon=NULL, selected=NULL, size=NULL, style=NULL, text=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultSelected=defaultSelected, disabled=disabled, loading_state=loading_state, onChange=onChange, onClick=onClick, renderIcon=renderIcon, selected=selected, size=size, style=style, text=text)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SelectableTag',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultSelected', 'disabled', 'loading_state', 'onChange', 'onClick', 'renderIcon', 'selected', 'size', 'style', 'text'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
