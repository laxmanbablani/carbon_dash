# AUTO GENERATED FILE - DO NOT EDIT

#' @export
notificationActionButton <- function(children=NULL, id=NULL, className=NULL, inline=NULL, loading_state=NULL, onClick=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, inline=inline, loading_state=loading_state, onClick=onClick, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'NotificationActionButton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'inline', 'loading_state', 'onClick', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
