# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tab <- function(children=NULL, id=NULL, as_=NULL, className=NULL, disabled=NULL, label=NULL, loading_state=NULL, onClick=NULL, onKeyDown=NULL, renderButton=NULL, renderIcon=NULL, secondaryLabel=NULL, style=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, disabled=disabled, label=label, loading_state=loading_state, onClick=onClick, onKeyDown=onKeyDown, renderButton=renderButton, renderIcon=renderIcon, secondaryLabel=secondaryLabel, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Tab',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'disabled', 'label', 'loading_state', 'onClick', 'onKeyDown', 'renderButton', 'renderIcon', 'secondaryLabel', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
