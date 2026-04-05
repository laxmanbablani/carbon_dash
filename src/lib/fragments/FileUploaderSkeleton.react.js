import React from 'react';
import { FileUploaderSkeleton as CarbonFileUploaderSkeleton } from '@carbon/react';

const FileUploaderSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFileUploaderSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFileUploaderSkeleton>
    );
};



export default FileUploaderSkeleton;
