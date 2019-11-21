class Cell
{ var data: int; }

class Counter
{
    ghost var shadow: int;
    ghost var footprint: set<object>;
    var incs: Cell;
    var decs: Cell;

    predicate Valid()
    reads this, footprint;
    {
        {this, incs, decs} <= footprint &&
        incs != decs && shadow == incs.data - decs.data
    }
    constructor()
    ensures Valid();
    ensures shadow == 0;
    ensures fresh(footprint);
    {
        var temp1, temp2 := new Cell, new Cell;
        temp1.data, temp2.data := 0, 0;
        incs, decs := temp1, temp2;
        shadow := 0;
        footprint := {this, incs, decs};
    } 

    method Inc() modifies footprint;
    requires Valid(); ensures Valid();
    ensures shadow == old(shadow) + 1;
    ensures fresh(footprint - old(footprint));
    { 
        incs.data := incs.data + 1;
        shadow := shadow + 1; 
    }

    method Dec() modifies footprint;
    requires Valid(); ensures Valid();
    ensures shadow == old(shadow) - 1;
    ensures fresh(footprint - old(footprint));
    { 
        decs.data := decs.data + 1;
        shadow := shadow - 1; 
    }

    method GetCounter() returns (x: int)
    requires Valid();
    ensures x == shadow;
    { x := incs.data - decs.data; }
}


method Verification()
{
    var c := new Counter();
    c.Inc();
    c.Inc();
    c.Dec();
    c.Inc();
    var i: int := c.GetCounter();
    assert i == c.shadow == 2;
}

