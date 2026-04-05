import React from 'react';
import { FileUploaderButton as CarbonFileUploaderButton } from '@carbon/react';

const FileUploaderButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFileUploaderButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFileUploaderButton>
    );
};



export default FileUploaderButton;
