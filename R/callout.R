# AUTO GENERATED FILE - DO NOT EDIT

#' @export
callout <- function(children=NULL, id=NULL, actionButtonLabel=NULL, className=NULL, kind=NULL, loading_state=NULL, lowContrast=NULL, onActionButtonClick=NULL, statusIconDescription=NULL, style=NULL, subtitle=NULL, title=NULL, titleId=NULL) {
    
    props <- list(children=children, id=id, actionButtonLabel=actionButtonLabel, className=className, kind=kind, loading_state=loading_state, lowContrast=lowContrast, onActionButtonClick=onActionButtonClick, statusIconDescription=statusIconDescription, style=style, subtitle=subtitle, title=title, titleId=titleId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Callout',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'actionButtonLabel', 'className', 'kind', 'loading_state', 'lowContrast', 'onActionButtonClick', 'statusIconDescription', 'style', 'subtitle', 'title', 'titleId'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
