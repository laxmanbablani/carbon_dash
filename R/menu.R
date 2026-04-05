# AUTO GENERATED FILE - DO NOT EDIT

#' @export
menu <- function(children=NULL, id=NULL, backgroundToken=NULL, border=NULL, className=NULL, label=NULL, loading_state=NULL, menuAlignment=NULL, mode=NULL, onClose=NULL, onOpen=NULL, open=NULL, size=NULL, style=NULL, target=NULL, x=NULL, y=NULL) {
    
    props <- list(children=children, id=id, backgroundToken=backgroundToken, border=border, className=className, label=label, loading_state=loading_state, menuAlignment=menuAlignment, mode=mode, onClose=onClose, onOpen=onOpen, open=open, size=size, style=style, target=target, x=x, y=y)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Menu',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'backgroundToken', 'border', 'className', 'label', 'loading_state', 'menuAlignment', 'mode', 'onClose', 'onOpen', 'open', 'size', 'style', 'target', 'x', 'y'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
