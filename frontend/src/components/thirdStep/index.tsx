import React, {useEffect, useState} from "react";
import { OtimizationResultType } from "../../utils/types";

export interface ThirdStepProps {
  otimizationResult: OtimizationResultType
}


export default function ThirdStep({otimizationResult}: ThirdStepProps) {

  return (
    <section className="flex flex-col w-1/3">
      <h2 className="text-heading-semibold-5 text-blue-100 mb-2">Fim!</h2>
      <div className="flex bg-gray-100 w-3/4 py-10 px-8 rounded-2xl">
        <div className="flex flex-col bg-white shadow-1 rounded-xl w-full py-10 px-8 rounded-2xl">
          <span className="text-body-semibold-1 mb-3">
            Resultado
          </span>
        </div>
      </div>
    </section>
  );
}
