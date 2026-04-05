# AUTO GENERATED FILE - DO NOT EDIT

#' @export
skeletonText <- function(children=NULL, id=NULL, className=NULL, heading=NULL, lineCount=NULL, loading_state=NULL, paragraph=NULL, style=NULL, width=NULL) {
    
    props <- list(children=children, id=id, className=className, heading=heading, lineCount=lineCount, loading_state=loading_state, paragraph=paragraph, style=style, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SkeletonText',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'heading', 'lineCount', 'loading_state', 'paragraph', 'style', 'width'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
