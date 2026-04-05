# AUTO GENERATED FILE - DO NOT EDIT

#' @export
toastNotification <- function(children=NULL, id=NULL, ariaLabel=NULL, caption=NULL, className=NULL, hideCloseButton=NULL, kind=NULL, loading_state=NULL, lowContrast=NULL, onClose=NULL, onCloseButtonClick=NULL, role=NULL, statusIconDescription=NULL, style=NULL, subtitle=NULL, timeout=NULL, title=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, caption=caption, className=className, hideCloseButton=hideCloseButton, kind=kind, loading_state=loading_state, lowContrast=lowContrast, onClose=onClose, onCloseButtonClick=onCloseButtonClick, role=role, statusIconDescription=statusIconDescription, style=style, subtitle=subtitle, timeout=timeout, title=title)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ToastNotification',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'caption', 'className', 'hideCloseButton', 'kind', 'loading_state', 'lowContrast', 'onClose', 'onCloseButtonClick', 'role', 'statusIconDescription', 'style', 'subtitle', 'timeout', 'title'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
