# AUTO GENERATED FILE - DO NOT EDIT

#' @export
actionableNotification <- function(children=NULL, id=NULL, actionButtonLabel=NULL, ariaLabel=NULL, caption=NULL, className=NULL, closeOnEscape=NULL, hasFocus=NULL, hideCloseButton=NULL, inline=NULL, kind=NULL, loading_state=NULL, lowContrast=NULL, onActionButtonClick=NULL, onClose=NULL, onCloseButtonClick=NULL, role=NULL, statusIconDescription=NULL, style=NULL, subtitle=NULL, title=NULL) {
    
    props <- list(children=children, id=id, actionButtonLabel=actionButtonLabel, ariaLabel=ariaLabel, caption=caption, className=className, closeOnEscape=closeOnEscape, hasFocus=hasFocus, hideCloseButton=hideCloseButton, inline=inline, kind=kind, loading_state=loading_state, lowContrast=lowContrast, onActionButtonClick=onActionButtonClick, onClose=onClose, onCloseButtonClick=onCloseButtonClick, role=role, statusIconDescription=statusIconDescription, style=style, subtitle=subtitle, title=title)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ActionableNotification',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'actionButtonLabel', 'ariaLabel', 'caption', 'className', 'closeOnEscape', 'hasFocus', 'hideCloseButton', 'inline', 'kind', 'loading_state', 'lowContrast', 'onActionButtonClick', 'onClose', 'onCloseButtonClick', 'role', 'statusIconDescription', 'style', 'subtitle', 'title'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
