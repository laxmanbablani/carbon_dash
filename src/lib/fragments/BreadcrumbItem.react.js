import React from 'react';
import { BreadcrumbItem as CarbonBreadcrumbItem } from '@carbon/react';

const BreadcrumbItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        href,
        isCurrentPage,
        ...otherProps
    } = props;
    return (
        <CarbonBreadcrumbItem
            id={id}
            className={className}
            style={style}
            href={href}
            isCurrentPage={isCurrentPage}
            {...otherProps}
        >
            {children}
        </CarbonBreadcrumbItem>
    );
};



export default BreadcrumbItem;
