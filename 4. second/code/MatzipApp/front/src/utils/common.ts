import {ForwardedRef} from 'react';

function mergeRefs<T>(...refs: ForwardedRef<T>[]) {
  return (node: T) => {
    refs.forEach(ref => {
      if (typeof ref === 'function') {
        ref(node);
      } else if (ref) {
        ref.current = node;
      }
    });
  };
}

export {mergeRefs};

// 복잡하다고 느끼면 react-merge-ref 이런 라이브러리를 써도 됨
