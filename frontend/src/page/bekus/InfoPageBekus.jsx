import './InfoPageBekus.css';

const InfoPageBekus = () => {
  return (
    <div className="info-page">
      <div className="left-panel"></div>
      <div className='text'>
        <p className='title'>Բեկուսի FP լեզու</p>
        <p>Նկարագրենք (M, C, X, T) քառյակը։</p>
        <p>Նախ սահմանենք A բազմությունը, որպես թվերի և իդենտիֆիկատրների բազմություն։ Գոյություն ունեն ատոմներ, որոնք ունեն որոշակի իմաստ, օրինակ՝ true (տրամաբանական "ճիշտ" արժեք), false (տրամաբանական "սխալ" արժեք), nil(դատարկ ցուցակ)։ </p>
        <p>M-ը անվանում ենք օբյեկտների բազմություն, որը սահմանվում է հետևյալ կերպ․</p>
        <div className='paymanner1'>
          <p>1. Եթե m ∈ A, ապա m ∈ M</p>
          <p>2․ ⊥ ∈ M։</p>
          <p>3. Եթե m1, m2, ..., mk ∈ M (k ≥ 0), ապա (m1, m2, ..., mk) ∈ M, և եթե որևէ i-ի համար (1 ≤ i ≤ k), mi = ⊥, ապա (m1, m2, ..., mk) = ⊥։</p>
          <p>4․ Ուրիշ օբյեկտներ չկան։</p>
        </div>
        <p>Եթե (m1, m2, ..., mk) ∈ M, k ≥ 0, ապա (m1, m2, ..., mk) կանվանենք ցուցակ, իսկ k-ն՝ նրա երկարություն։ Ցուցակը, որի երկարությունը հավասար է0-ի կանվանենք դատարկ ցուցակ, որը կնշանակենք nil ատոմով։</p>
        <p>Այժմ նկարագրենք C բազմությունը։</p>
        <p>C = M ∪ C1 ∪ C2, որտեղ C1-ըառաջին կարգի հաստատուններ են, իսկ C2-ը՝ երկրորդ կարգի։ Նկարագրենք դրանք։</p>
        <p>C1 = {`{si | i ≥ 1}`} ∪ {`{id, tl, apndl, apndr, null, atom, eq, '+', '-', /, *, and, or, not, ...}`}</p>
        <p>Նշենք, որ եթե f ∈ M1, ապա f ∈ {'[M->M]'}: Սահմանենք դրանք ցանկացած m ∈ M համար․</p>
        <p>Selector Functions (ընդհարման ֆունկցիաներ)</p>
        <div className='functions'>
          <p>si(m) = </p>
          <p>mi, եթե m = (m1, m2, ..., mk)</p>
          <p>1 ≤ i ≤ k, k ≥ 1, հակառակ դեպքում՝ ⊥</p>
        </div>
        <p>Identity (նույնություն)</p>
        <div className='functions'>
          <p>id(m) = m</p>
        </div>
        <p>Tail (պոչ)</p>
        <div className='functions'>
          <p>tl(m) = nil, եթե m = (m1), (m2, m3, ..., mk), եթե m = (m1, m2, ..., mk), k {'>'} 1, մնացած դեպքերում՝ ⊥</p>
        </div>
        <p>Append Left (ավելացնել օբյեկտ ձախից)</p>
        <div className='functions'>
          <p>apndl(m) = (m0, m1, ..., mk), եթե m = (m0, (m1, m2, ..., mk)), k ≥ 1, (m0), եթե m = (m0, nil), մնացած դեպքերում՝ ⊥</p>
        </div>
        <p>Append Right (ավելացնել օբյեկտ աջից)</p>
        <div className='functions'>
          <p>appndr(m) = (m1, ..., mk, m0), եթե m = (m0, (m1, m2, ..., mk)), k ≥ 1, եթե m = (m0, nil), մնացած դեպքերում՝ ⊥</p>
        </div>
        <p>Null (դատարկ)</p>
        <div className='functions'>
          <p>null(m) = true, եթե m = nil, fasle, եթե m ≠ ⊥ և m ≠ nil, մնացած դեպքերում՝ ⊥</p>
        </div>
        <p>Atom (ատոմ)</p>
        <div className='functions'>
          <p>atom(m) = true, m ∈ A, false, եթե m ∉ A և m ≠ ⊥, մնացած դեպքերում՝ ⊥</p>
        </div>
        <p>Equals (հավասար)</p>
        <div className='functions'>
          <p>eq(m) = true, եթե m = (m1, m2) և m1 = m2, false, եթե m = (m1, m2) և m1 ≠ m2, մնացած դեպքերում՝ ⊥</p>
          <p>+(m) = m1 + m2, եթե m = (m1, m2) և m1, m2-ը թվեր են, մնացած դեպքերում՝ ⊥</p>
          <p>֊(m) = m1 - m2, եթե m = (m1, m2) և m1, m2-ը թվեր են, մնացած դեպքերում՝ ⊥</p>
          <p>*(m) = m1 * m2, եթե m = (m1, m2) և m1, m2-ը թվեր են, մնացած դեպքերում՝ ⊥</p>
          <p>and(m) = m1 & m2, եթե m = (m1, m2) և m1, m2 ∈ {'{true, false}'}, մնացած դեպքերում՝ ⊥</p>
          <p>or(m) = m1 ∨ m2, եթե m = (m1, m2) և m1, m2 ∈ {'{true, false}'}, մնացած դեպքերում՝ ⊥</p>
          <p>not(m) = true, եթե m = false, false, եթե m = true, մնացած դեպքերում՝ ⊥</p>
        </div>
        <p>Նկարագրենք C1 = {'{comp, constr, const, cond, ... }'} բազմությունը, որի էլեմենտները ֆունկցիոնալներ են և սահմանվում են հետևյալ կերպ․</p>
        <p>Composition (Կոմպոզիցիա)</p>
        <p>comp ∈ [[M→M]^2→[M→M]] և ցանկացած g, h ∈ [M→M] ֆունկցիաների համար comp(g, h) = f ∈ [M→M], որը որոշվում է հետևյալ կերպ․ ցանկացած m ∈ M համար</p>
        <div className='functions'>
          <p>f(m) = g(h(m))</p>
        </div>
        <p>Construction (կառուցում)</p>
        <p>constr∈[[M→M]^2→[M→M]] և ցանկացած g,h ∈ [M→M] ֆունկցիաների համար constr(g,h) = f ∈ [M→M], որը որոշվում է հետևյալ կերպ․ ցանկացած m ∈ M համար</p>
        <div className='functions'>
          <p>f(m) = (g(m) h(m))</p>
        </div>
        <p>Constant (հաստատուն)</p>
        <p>const ∈ [M→[M→M]] և ցանկացած m0 ∈ M հաստատունի համար const(m0) = f ∈ [M→M], որը որոշվում է հետևյալ կերպ․ ցանկացած m ∈ M համար</p>
        <div className='functions'>
          <p>f(m) = m0, եթե m ≠ ⊥, ⊥, եթե m = ⊥</p>
        </div>
        <p>Condition (պայման)</p>
        <p>cond ∈ [[M→M]^3→[M→M]] և ցանկացած p, g, h ∈ [M→M] ֆունկցիաների համար cond(p, g, h) = f ∈[M→M], որը որոշվում է հետևյալ կերպ․ ցանկացած m ∈ M համար</p>
        <div className='functions'>
          <p>f(m) = g(m), եթե p(m) = true, h(m), եթե p(m) = false, մնացած դեպքերում՝ ⊥</p>
        </div>
        <p>{'X = {Fi | Fi ∈ V[M→M], i ≥ 1}'}</p>
        <p>T ⊂ Λ(C, X), որտեղ T-ն այն թերմերի բազմությունն է, որոնցում λ չի օգտագործվում, այսինքն՝ թերմի սահմանման 4-րդ կետը չի օգտագործվում, իսկ M բազմության օբյեկտները անդիսանում են միայն որպես const ֆունկցիոնալի արգումենտի արժեք։</p>
        <p>Օրինակ 1։ Դիտարկենք s ∈ [M→M] ֆունկցիան, որը սահմանվում է հետևյալ կերպ․ ցանկացած m ∈ M համար</p>
        <p>s(m) = m + 1, եթե m֊ը թիվ է, մնացած դեպքերում՝ ⊥</p>
        <p>Այն հանդիսանում է հետևյալ հավասարման լուծում․</p>
        <div className='functions'>
          <p>F1 = comp(+, constr(id, const(1)) )</p>
        </div>
        <p>Օրինակ 2։ Դիտարկենք ! ∈ [M→M] ֆակտորիալ ֆունկցիան, որը սահմանվում է հետևյալ կերպ․ ցանկացած m ∈ M համար</p>
        <p>!(m) = !m, եթե m-ը բնական թիվ է, մնացած դեպքերում՝ ⊥</p>
        <p>Այն հանդիսանում է հետևյալ հավասարումների համակարգի լուծման գլխավոր ֆունկցիա․</p>
        <div className='functions'>
          <p>F1 = cond(comp(eq, constr(id, const(0))), const(1), F2)</p>
          <p>F2 = comp(*, constr(id, comp(F1, comp(-, constr(id, const(1))))))</p>
        </div>
        <p>Օրինակ 3։ Դիտարկենք atoms ∈ [M→M] ֆունկցիան, որը սահմանվում է հետևյալ կերպ․ ցանկացած m ∈ M համար</p>
        <p>atoms(m) = n, եթե m֊ը ցուցակ է և n֊ը m ցուցակում ատոմների քանակն է, մնացած դեպքերում՝ ⊥</p>
        <p>Այն հանդիսանում է հետևյալ հավասարումների համակարգի լուծման գլխավոր ֆունկցիա․</p>
        <div className='functions'>
          <p>F1 = cond(null, const(0), cond(comp(atom,s1), F2, F3))</p>
          <p>F2 = comp(+, constr(const(1), comp(F1, tl)))</p>
          <p>F3 = comp(+, constr(comp(F1,s1), comp(F1, tl)))</p>
        </div>
        <p>Օրինակ 4։ Դիտարկենք reverse ∈ [M→M] ֆունկցիան, որը սահմանվում է հետևյալ կերպ․ ցանկացած m ∈ M համար</p>
        <p>{'reverse(m) = (mk ... m1), եթե m=(m1 ... mk), k>0, nil, եթե m=nil, մնացած դեպքերում՝ ⊥'}</p>
        <p>Այն հանդիսանում է հետևյալ հավասարման լուծում</p>
        <div className='functions'>
          <p>F1 = cond(null, const(nil), comp(apndr, constr(s1, comp(F1, tl))))</p>
        </div>
      </div>

    </div>
  );
};

export default InfoPageBekus;