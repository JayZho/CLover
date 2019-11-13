class Tub
{
 ghost var IsEmpty: bool;
 ghost var IsPart: bool;
 ghost var IsFull: bool;
 ghost var Tap: bool; // on == true, off == false
 ghost var Plug: bool; // in == true, out == false
 predicate Valid()
 reads this
 {((IsEmpty && !IsPart && !IsFull) ||
 (!IsEmpty && IsPart && !IsFull) ||
 (!IsEmpty && !IsPart && IsFull)) // mutually exclusive
 && !(Tap && !Plug) // be safe: don't allow tap on and plug out
 && !(Plug && IsEmpty) // be safe: don't allow plug in when tub empty
 && !(Tap && IsFull) // be safe: don't allow tap on and full tub
 }
A tub 