import React from 'react';
import { Breadcrumb as CarbonBreadcrumb } from '@carbon/react';

const Breadcrumb = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        noTrailingSlash,
        ...otherProps
    } = props;
    return (
        <CarbonBreadcrumb
            id={id}
            className={className}
            style={style}
            noTrailingSlash={noTrailingSlash}
            {...otherProps}
        >
            {children}
        </CarbonBreadcrumb>
    );
};



export default Breadcrumb;
