# AUTO GENERATED FILE - DO NOT EDIT

#' @export
formGroup <- function(children=NULL, id=NULL, className=NULL, disabled=NULL, invalid=NULL, legendId=NULL, legendText=NULL, loading_state=NULL, message=NULL, messageText=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, disabled=disabled, invalid=invalid, legendId=legendId, legendText=legendText, loading_state=loading_state, message=message, messageText=messageText, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FormGroup',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'disabled', 'invalid', 'legendId', 'legendText', 'loading_state', 'message', 'messageText', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
