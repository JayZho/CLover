module Helper {
  //export Spec provides addOne, addOne_result
  export Body provides getType
  
  class BloodBag 
  {
    var bloodType: seq<char>;
    
    method getType() returns (t: seq<char>){
      return bloodType;
    }
  }

  type BloodBag
  method getType()
  function bloodType(): seq<char>
}


class BloodType
{
  //import opened Helper
  
  var bloodType: seq<char>;
  var quantity: int;
  var bloodBags: array<Helper.BloodBag>;
  var critical: int;
  
  
  predicate Valid() //class invariant
    reads this;
  { 
    //blood type is one of the following types
    (bloodType == "A" || bloodType == "B" || bloodType == "AB" || bloodType == "O")
    
    //critical level has to be a positive number
    && (critical > 0)
    
    //consistency between quantity and size of bloodBags
    && (quantity == bloodBags.Length)
    
    //all blood bags stored under this class is of matching type
    && (forall index:: 0<=index<bloodBags.Length ==> (bloodBags[index].getType() == bloodType))
  }
  
  constructor (crit: int, blood: seq<char>)
    requires crit > 0;
    requires blood == "A" || blood == "B" || blood == "AB" || blood == "O"
    
    ensures Valid();
    ensures quantity == bloodBags.Length == 0; //starts with empty storage
  { 
    critical := crit; 
    bloodType := blood;
    quantity := 0;
    bloodBags := new Helper.BloodBag[0];
  }


  method removeBloodBag(bag: BloodBag)
  modifies this;

  requires Valid(); 
  requires exists x:: 0<=x<bloodBags.Length && bloodBags[x]==bag && forall y:: (0<=y<bloodBags.Length && y!=x) ==> bloodBags[y] != bag;
  
  ensures Valid();
  ensures forall index:: 0<=index<bloodBags.Length ==> (bloodBags[index] != bag);
  ensures bloodBags.Length == old(bloodBags.Length) - 1;
  {
    var i := 0;
    var j := 0;
    var newBloodBags: array := new BloodBag[bloodBags.Length-1];
    
    while i < bloodBags.Length
    invariant 0<=i<=bloodBags.Length
    invariant exists x:: 0<=x<bloodBags.Length && bloodBags[x]==bag && forall y:: (0<=y<bloodBags.Length && y!=x) ==> bloodBags[y] != bag
    invariant (i == j) ==> (forall x:: 0<=x<i ==> newBloodBags[x] == bloodBags[x])
    invariant 
    {
      if bloodBags[i] != bag {
        newBloodBags[j] := bloodBags[i];
        j := j + 1;
      }
      i := i + 1;
    }

    assert (newBloodBags.Length == bloodBags.Length - 1);
    bloodBags := newBloodBags;


  }
  
    
}
