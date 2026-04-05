# AUTO GENERATED FILE - DO NOT EDIT

#' @export
inlineNotification <- function(children=NULL, id=NULL, className=NULL, hideCloseButton=NULL, kind=NULL, loading_state=NULL, lowContrast=NULL, onClose=NULL, onCloseButtonClick=NULL, role=NULL, statusIconDescription=NULL, style=NULL, subtitle=NULL, title=NULL) {
    
    props <- list(children=children, id=id, className=className, hideCloseButton=hideCloseButton, kind=kind, loading_state=loading_state, lowContrast=lowContrast, onClose=onClose, onCloseButtonClick=onCloseButtonClick, role=role, statusIconDescription=statusIconDescription, style=style, subtitle=subtitle, title=title)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'InlineNotification',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'hideCloseButton', 'kind', 'loading_state', 'lowContrast', 'onClose', 'onCloseButtonClick', 'role', 'statusIconDescription', 'style', 'subtitle', 'title'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
