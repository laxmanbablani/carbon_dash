# AUTO GENERATED FILE - DO NOT EDIT

#' @export
progressStep <- function(children=NULL, id=NULL, className=NULL, complete=NULL, current=NULL, description=NULL, disabled=NULL, index=NULL, invalid=NULL, label=NULL, loading_state=NULL, onClick=NULL, overflowTooltipProps=NULL, secondaryLabel=NULL, style=NULL, tooltipId=NULL, translateWithId=NULL) {
    
    props <- list(children=children, id=id, className=className, complete=complete, current=current, description=description, disabled=disabled, index=index, invalid=invalid, label=label, loading_state=loading_state, onClick=onClick, overflowTooltipProps=overflowTooltipProps, secondaryLabel=secondaryLabel, style=style, tooltipId=tooltipId, translateWithId=translateWithId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ProgressStep',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'complete', 'current', 'description', 'disabled', 'index', 'invalid', 'label', 'loading_state', 'onClick', 'overflowTooltipProps', 'secondaryLabel', 'style', 'tooltipId', 'translateWithId'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
